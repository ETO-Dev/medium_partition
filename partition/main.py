def main():
    try:
        with open('response.txt', 'r') as file:
            for line in file:
                if 'Modified_Date' in line:
                    # ('Modified_Date', ':', '2024-03-11 16:10:58.909413 +00:00') 🎈✨
                    key, sep, value = line.partition(':')
                    return print(value.strip())
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist")
    
if __name__ == "__main__":
    main()