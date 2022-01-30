#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <vector>
#include <map>

namespace constants {
    constexpr int kmer = 3;
}

using InputFasta = std::vector<std::pair<std::string, std::string>>;
using Graph = std::map<std::string, std::vector<std::string>>;

InputFasta readInputFasta(const std::string& filePath) {
    InputFasta fastaSeq;

    std::ifstream inputFasta(filePath, std::ios::in);

    std::string tempLine;
    while (std::getline(inputFasta, tempLine).good()) {
        std::string id, seq;

        if (tempLine.empty()) {
            continue;
        }

        if (tempLine[0] == '>') {
            id = tempLine;
        }
        
        std::string seqLine;
        while (inputFasta.peek() != '>' && !inputFasta.eof()) {
            std::getline(inputFasta, seqLine);
            seq += seqLine;
        }

        fastaSeq.emplace_back(id, seq);
    }

    inputFasta.close();

    return fastaSeq;
}

Graph constructDirectedGraphFromInputFasta(InputFasta& fasta) {
    Graph diGraph;

    for (int i = 0; i < fasta.size() - 1; i++) {
        for (int j = i + 1; j < fasta.size(); j++) {
            std::string kmerSuffix = fasta[i].second.substr(fasta[i].second.size() - constants::kmer);
            std::string kmerPrefix = fasta[j].second.substr(0, constants::kmer);
            if (kmerSuffix == kmerPrefix) {
                diGraph[fasta[i].first].push_back(fasta[j].first);
            } 

            std::string switchedKmerSuffix = fasta[j].second.substr(fasta[j].second.size() - constants::kmer);
            std::string switchedKmerPrefix = fasta[i].second.substr(0, constants::kmer);
            if (switchedKmerPrefix == switchedKmerSuffix) {
                diGraph[fasta[j].first].push_back(fasta[i].first);
            }
        }
    }

    return diGraph;
}

void printGraph(const Graph& graph) {
    for (const auto& [node, children] : graph) {
        for (const auto& child : children) {
            std::cout << node.substr(1) << " " << child.substr(1) << std::endl;
        }
    }
}

int main([[maybe_unused]]int argc, [[maybe_unused]]char* argv[]) {
    if (argc < 2) {
        std::cerr << "\nUsage: " << argv[0] << " -> must pass file path!\n" << std::endl;
        return EXIT_FAILURE;
    }

    std::string filePath = argv[1];

    // const std::string filePath = "C:\\Users\\user\\AppData\\Local\\Temp\\rosalind_grph-1.txt";

    InputFasta sequences = readInputFasta(filePath);

    Graph graph = constructDirectedGraphFromInputFasta(sequences);

    printGraph(graph);

    return EXIT_SUCCESS;
}

// C:\Users\user\AppData\Local\Temp\rosalind_grph.txt
