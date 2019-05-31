import html_parse

if __name__ == '__main__':
    program = input("Would you like to run the index or the query? ")
    while True:
        if program == "index":
            html_parse()
            break
        elif program == "query":
            query = input("Enter Query: ")
            print(query)
            break
        else:
            program = input("Invalid response! Would your like to run the index or the query")
            continue
    
    
