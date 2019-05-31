import html_parse
import Query
import sys

if __name__ == '__main__':
    program = input("Would you like to run the index or the query? ")
    while True:
        if program == "index":
            sys.stdout = open("output2.txt", "w")  # OUTPUT to file called output.txt
            i = html_parse.InvertedIndex() 
            i.html_parse()
            #i.print_inverted_ind()
            i.calculate_tf_idf()
            i.print_inverted_ind()
            break
        elif program == "query":
            usr_in = input("Enter Query: ")
            query = Query.Query(usr_in)
            query.run_query()
            break
        else:
            program = input("Invalid response! Would your like to run the index or the query")
            continue
    
    
