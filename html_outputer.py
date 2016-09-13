import redis


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        return self.datas

    def output_to_redis(self):
        db = redis.Redis(host='192.168.15.132', port=6379, db=0)
        for data in self.datas:
            db.hset(data['url'], data['title'], data['summary'])

    def output_to_local_file(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<head>")
        fout.write('<title>python web_spider</title>')
        fout.write("<meta charset='utf-8'>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
