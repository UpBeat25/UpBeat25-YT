#include <iostream>
#include <filesystem>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
namespace fs = std::filesystem;

void storeToFile(const std::vector<std::string> &filenames, const std::string &filename)
{
    std::ofstream outFile(filename);
    if (!outFile.is_open())
    {
        std::cerr << "Error: Unable to open file for writing." << std::endl;
        return;
    }
    for (const std::string &name : filenames)
    {
        outFile << name << std::endl;
    }
    outFile.close();
}

std::vector<std::string> readFromFile(const std::string &filename)
{
    std::vector<std::string> filenames;
    std::ifstream inFile(filename);
    if (!inFile.is_open())
    {
        std::cerr << "Error: Unable to open file for reading." << std::endl;
        return filenames;
    }
    std::string line;
    while (std::getline(inFile, line))
    {
        filenames.push_back(line);
    }
    inFile.close();
    return filenames;
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        std::cerr << "Usage: " << argv[0] << " init|add|commit" << std::endl;
        return 1;
    }

    std::string command = argv[1];
    std::vector<std::string> files;

    if (command == "init")
    {
        if (fs::create_directory(".bitlo") == 0)
        {
            std::cout << "Directory created successfully.\n";
        }
        else
        {
            std::cerr << "Failed to create directory!\n";
        }
        if (fs::exists(".bitlo/bucket.txt"))
        {
            return 0;
        }
        else
        {
            std::ofstream outFile(".bitlo/bucket.txt");
            if (outFile.is_open())
            {
                std::cout << "Success!" << std::endl;
                // Close the file stream
                outFile.close();
            }
        }
    }
    else if (command == "add")
    {
        // Assuming you want to add files listed in the console
        std::string filename;
        std::cout << "Enter filenames (type 'end' to finish):" << std::endl;
        while (true)
        {
            std::getline(std::cin, filename);
            if (filename == "end")
            {
                break;
            }
            else if (filename == ".")
            {
                fs::path directoryPath(".");
                if (!fs::exists(directoryPath) || !fs::is_directory(directoryPath))
                {
                    std::cerr << "Directory not found or invalid." << std::endl;
                    return 1;
                }
                for (const auto &entry : fs::directory_iterator(directoryPath))
                {
                    if (fs::is_regular_file(entry.path()))
                    {
                        if (entry.path().string() == ".bitlo")
                        {
                            continue;
                        }
                        else
                        {
                            files.push_back(entry.path().string());
                        }
                    }
                }
                break;
            }
            files.push_back(filename);
        }

        storeToFile(files, ".bitlo/bucket.txt");
    }
    else if (command == "commit")
    {
        std::string commit_msg;
        std::cout << "Commit Message: ";
        std::getline(std::cin, commit_msg);
        if (commit_msg.empty())
        {
            std::cout << "Commit Message Cannot Be Nil";
            return 1;
        }
        fs::path destinationDirectory(commit_msg);
        fs::path bitlo(".bitlo");
        if (fs::exists(bitlo / destinationDirectory))
        {
            std::cout << "Choose a new Commit Message";
            return 1;
        }
        fs::create_directories(bitlo / destinationDirectory);

        for (const std::string &file : readFromFile(".bitlo/bucket.txt"))
        {
            fs::path filePath(file);
            fs::path destinationPath = bitlo / destinationDirectory / filePath.filename();
            fs::copy_file(filePath, destinationPath);
        }
        std::string comm = "tar -czvf .bitlo/" + commit_msg + ".tar.gz -C .bitlo " + commit_msg;
        system(comm.c_str());
        fs::remove_all(bitlo / destinationDirectory);
        fs::remove(".bitlo/bucket.txt");
        std::ofstream outFile(".bitlo/bucket.txt");
        if (outFile.is_open())
        {
            std::cout << "Success!" << std::endl;
            outFile.close();
        }
    }
    else if (command == "del_version")
    {
        std::string version;
        std::cout << "Version Name: ";
        std::getline(std::cin, version);
        if (version.empty())
        {
            std::cout << "Version Cannot Be Nil";
            return 1;
        }
        fs::remove(version + ".tar.gz");
    }
    else if (command == "restore")
    {
        std::string version;
        std::cout << "Version Name: ";
        std::getline(std::cin, version);
        if (version.empty())
        {
            std::cout << "Version Cannot Be Nil";
            return 1;
        }
        string commandsss = "tar -xzvf " + version + ".tar.gz";
        system(commandsss.c_str());
    }
    else
    {
        std::cerr << "Invalid Response";
        return 1;
    }
    return 0;
}
