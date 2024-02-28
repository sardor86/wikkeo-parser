from parser import Parser


def main():
    parser = Parser()
    print(parser.get_category())
    a = parser.get_products_list('Электроника')
    for i in a:
        print(parser.get_product_details(i['url']))


if __name__ == "__main__":
    main()
