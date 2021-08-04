По указанной в задаче ссылке скачиваются файлы, распаковываются (я делал через unzip в Ububntu 18 LTS).
При попытке прогрузить через HUE веб-интерфейс, загрузка тормозится из-за ограничений в 64MB.
Ссылка на проблему:
https://community.cloudera.com/t5/Support-Questions/Can-not-upload-file-greater-than-64MB-via-FileBrowser-in-HUE/td-p/118856

В итоге файлы нужно переместить из локальной файловой системы в hdfs через CLI,  hdfs dfs -moveFromLocal <local src>   <dest(on hdfs)>