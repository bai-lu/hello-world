import html_outputer
import html_parser
import html_downloader
import url_manager
from multiprocessing import Pool
import time,os

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self):
        if self.urls.has_new_url():
            print('pid is %s' % os.getpid())
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
        self.outputer.output_to_local_file()

if __name__ == '__main__':
    root_url = "http://192.168.15.132/w3school/index.html"
    obj_spider = SpiderMain()
    obj_spider.urls.add_new_url(root_url)
    begin = time.time()
    p=Pool(4)
    for i in range(500):
        p.apply_async(obj_spider.craw, args=())
    p.close()
    p.join()
    end = time.time()
    use = end - begin
    print('use %s s' % use)
