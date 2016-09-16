import html_outputer
import html_parser
import html_downloader
import url_manager
import time


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print("craw %d : %s" % (count, new_url))
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
            if count == 500:
                break
            count += 1
        # self.outputer.output_to_redis()
        self.outputer.output_to_local_file()

if __name__ == '__main__':
    root_url = "http://192.168.15.132/w3school/index.html"
    obj_spider = SpiderMain()
    begin = time.time()
    obj_spider.craw(root_url)
    end = time.time()
    use = end - begin
    print('use %s s' % use)
