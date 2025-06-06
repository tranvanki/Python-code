#task 1
def create_file():
    "create a file and store any 10 number in it"
    # with open('data.txt', 'w') as file:
    #     for i in range(10):
    #         file.write(f"{i + 1}\n")  # Writing  1 to 10, each on a new line
    with open('data.txt','w') as file:
        for i in range(10):
            file.write(f"{i * 2}\n")
def read_file():
    with open('data.txt', 'r') as file:
        content = file.readlines()
    content = [int(num.strip()) for num in content]  # Convert strings to integers
    return content
if __name__ == "__main__":
    create_file()  # Create the file with content
    content = read_file()  # Read the content from the file
    print("content read from the file:", content)  # Print the content to verif