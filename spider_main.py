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
            try:
                print('pid is %s' % os.getpid())
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # print(new_urls,new_data)
                test=self.urls.add_new_urls(new_urls)
                print(test)
                test=self.outputer.collect_data(new_data)
                print(test)
            except:
                print("craw failed")
        # self.outputer.output_to_redis()
        self.outputer.output_to_local_file()

if __name__ == '__main__':
    begin=time.time()
    spider = SpiderMain()
    root_url = "http://baike.baidu.com/view/21087.htm"
    spider.urls.add_new_url(root_url)
    p=Pool(4)
    for i in range(2):
        p.apply_async(spider.craw, args=())
    p.close()
    p.join()
    p.terminate()
    end=time.time()
    use=end-begin
    print('cost time %s s' % use)
