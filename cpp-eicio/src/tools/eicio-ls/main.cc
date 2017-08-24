#include <unistd.h>
#include <iostream>

#include "eicio/reader.h"

void printUsage() {
    std::cerr << "Usage: eicio-ls [options] <input eicio file>\n";
    std::cerr << "options:\n";
    std::cerr << "  -e int\n";
    std::cerr << "    	list specified event, numbered consecutively from the start of the file or stream "
                 "(default -1)\n";
    std::cerr << "  -g	decompress the stdin input with gzip\n";
    std::cerr << std::endl;
}

int main(int argc, char **argv) {
    bool gzip = false;
    int event = -1;

    int opt;
    while ((opt = getopt(argc, argv, "e:gh")) != -1) {
        switch (opt) {
            case 'e':
                event = atoi(optarg);
                break;
            case 'g':
                gzip = true;
                break;
            default:
                printUsage();
                exit(EXIT_FAILURE);
        }
    }

    std::string inputFilename;
    if (optind < argc) {
        inputFilename = argv[optind];
    } else {
        printUsage();
        exit(EXIT_FAILURE);
    }

    eicio::Reader *reader;
    if (inputFilename.compare("-") == 0)
        reader = new eicio::Reader(STDIN_FILENO, gzip);
    else
        reader = new eicio::Reader(inputFilename.c_str());

    bool singleEvent = false;
    if (event >= 0) {
        singleEvent = true;
        reader->Skip(event);
    }

    while (auto event = reader->Get()) {
        event->GetHeader()->PrintDebugString();

        for (auto name : event->GetNames()) {
            auto coll = event->Get(name);
            if (coll != NULL) {
                coll->PrintDebugString();
            }
        }

        delete event;

        if (singleEvent) break;
    }

    delete reader;
    return EXIT_SUCCESS;
}
