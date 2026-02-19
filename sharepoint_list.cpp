//NOT FINISHED: I need to update how the user input works

#include <iostream>
#include <string>

using namespace std;

string formatEmails(string input) {
    string target = "bison.howard.edu";
    size_t pos = input.find(target);
    int emailCount = 0;
    
    while (pos != string::npos) {
        input.insert(pos + target.length(), ";");
        emailCount++;
        
        pos = input.find(target, pos + target.length() + 1);

        if (emailCount == 50) {
            input.insert(pos, "\n\n");
            pos += 2;
            emailCount = 0;
        }
    }

    return input;
}

int main() {
    string rawData = "";
    cout << "Input emails here: ";
    cin >> rawData;
    cout << endl;
    cout << formatEmails(rawData) << endl;
    
    return 0;

}
