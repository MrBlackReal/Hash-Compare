import sys
import hashlib

BUF_SIZE = 65536;

# This is the little HashFunciton
def hashFile(file):
    sha256 = hashlib.sha256();

    with open(file, "rb") as f:
        while True:
            data = f.read(BUF_SIZE);

            if not data:
                break;

            sha256.update(data);

    f.close();
    return sha256.hexdigest();

# We are getting the files with the args.
# python main.py C:/path/to/file1 C:/path/to/file2
file1 = sys.argv[1];
file2 = sys.argv[2]

if __name__ == "__main__":
    f1_hash = "0x" + hashFile(file1);
    f2_hash = "0x" + hashFile(file2);

    # Check if the hashes are the same.
    if f1_hash == f2_hash:
        print("The files are the same!");
        print(f"Hash: {f1_hash}");
    else: # if not then we print them.
        print("The files are different!");
        print(f"Hash of {file1}: {f1_hash}");
        print(f"Hash of {file2}: {f2_hash}");
