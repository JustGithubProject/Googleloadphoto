from icrawler.builtin import GoogleImageCrawler


def google_load_img(search_photo):
    crawler = GoogleImageCrawler(storage={'root_dir': 'images'})
    crawler.crawl(keyword=search_photo)


def main():
    search_photo = input("Enter: ")
    google_load_img(search_photo)


if __name__ == "__main__":
    main()
