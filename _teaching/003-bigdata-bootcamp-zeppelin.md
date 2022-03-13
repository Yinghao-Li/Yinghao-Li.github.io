---
title: "Using Zeppelin in Docker"
collection: teaching
type: "Bootcamp"
permalink: /teaching/003-bigdata-bootcamp-zeppelin
venue: "Georgia Tech, School of CSE"
date: 2022-02-27
location: "Atlanta, GA"
toc: true
show: true
---

{% include user_def %}

> References: [[Source website 1](http://chaozhang.org/bigdata-bootcamp/docs/sessions/zeppelin-intro/), [Source website 2](http://chaozhang.org/bigdata-bootcamp/docs/sessions/zeppelin-tutorial/)].

## 1. Start the Docker image

Please prepare your docker environment and start your zeppelin service.
The instructions can be found in [this section]({{base_path}}/teaching/002-bigdata-bootcamp-docker).

### 1.1. Share Folders

You can use shared folders between your local OS and the virtual environment on Docker.
These folders can be used to access data from your local and to save data after you exit/destroy your virtual environment.
Use `-v` option to make shared folder from an existing local folder and a folder in virtual environment:

```bash
-v <local_folder:vm_folder>
```

You should use the absolute path for `vm_folder`, but it does not need to exist.
For example, if want to use `~/Data/` in my local OS as the shared folder connected with `/sample_data/` in VM, I can start a container as following:

```bash
docker run -it --privileged=true \
  --cap-add=SYS_ADMIN \
  -m 8192m -h bootcamp1.docker \
  --name bigbox -p 2222:22 -p 9530:9530 -p 8888:8888\
  -v /path/to/Data/:/sample_data/ \
  sunlab/bigbox:latest \
  /bin/bash
```

## 2. Install and start Zeppelin service

If you have not installed Zeppelin, you can install it with

```bash
/scripts/install-zeppelin.sh
```

Then, you can start Zeppelin service with

```bash
/scripts/start-zeppelin.sh
```

{{ hint_warning }}
Make sure you have already started other necessary services with `./scripts/start-services.sh` before installing Zeppelin.
{{ _hint }}

In addition, we need to create a HDFS folder for the user `zeppelin` as:

```bash
sudo su - hdfs  # switch to user 'hdfs'
hdfs dfs -mkdir -p /user/zeppelin  # create folder in hdfs
hdfs dfs -chown zeppelin /user/zeppelin  # change the folder owner
exit
```

You can check whether it has been created or not by using:

```bash
hdfs dfs -ls /user/
```

## 3. Open Zeppelin Notebook in your browser

Once you have started Zeppelin service and have created the HDFS folder for Zeppelin, you can access Zeppelin Notebook using your local web browser.

Open your web browser, and type in the address:

```bash
<host-ip>:<port-for-zeppelin>
```

For example, the address is `192.168.99.100:9530` if the IP address assigned to your Docker container is `192.168.99.100`, and the port number assigned to Zeppelin service is `9530` as default in our Docker image.

{{ hint_info }}
You can check your docker host IP address using `ifconfig` (Linux/macOS) or `ipconfig` (Windows).
The IP address is located at `Ethernet adapter vEthernet->IPv4 Address`.

In fact, the docker host IP address is automatically mapped to url [http://host.docker.internal](http://host.docker.internal).
So, a simpler approach is directly using the url [http://host.docker.internal:9530](http://host.docker.internal:9530) to access Zeppelin Notebook ([reference](https://docs.docker.com/desktop/windows/networking/)).
{{ _hint }}

Once you navigate to that IP address with the port number, you will see the front page of Zeppelin like:
![zeppelin-frontpage]({{base_path}}/images/teaching/spark_images/zeppelin/frontpage.png)

## 4. Create a new Notebook

Click on 'Create new note', and give a name, click on 'Create Note':
Then, you will see a new blank note:

![zeppelin-new]({{base_path}}/images/teaching/spark_images/zeppelin/create.gif)

Next, click the gear icon on the top-right, interpreter binding setting will be unfolded.
Default interpreters will be enough for the most of cases, but you can add/remove at 'interpreter' menu if you want to. Click on 'Save' once you complete your configuration.

![zeppelin-interpreters]({{base_path}}/images/teaching/spark_images/zeppelin/settings.gif)

## 5. Basic usage

You can click the gear icon at the right side of the paragraph. If you click 'Show title' you can give a title as you want for each paragraph.
Try to use other commands also.

![zeppelin-title]({{base_path}}/images/teaching/spark_images/zeppelin/menu.gif)

### 5.1. Text note

Like other Notebooks, e.g., Jupyter, we can put some text in a paragraph by using `md` command with Markdown syntax:

```
%md
<some text using markdown syntax>
```

Afterwards, click the `play` button or use key combination `Shift+Enter` to run the paragraph.
It will show formatted Markdown text.
You can also choose to show or hide editor for better visual effect.

![zeppelin-text]({{base_path}}/images/teaching/spark_images/zeppelin/text.gif)

### 5.2. Scala code

If you bind default interpreters, you can use scala codes as well as Spark API in a paragraph directly:

![zeppelin-scala]({{base_path}}/images/teaching/spark_images/zeppelin/scala.png)

Again, do not forget to actually run the paragraph.

### 5.3. Possible Error

If you meet an error related with HDFS, please check whether you have created HDFS user folder for 'zeppelin' as described above.

## 6. Load Data Into Table

We can use SQL query statements for easier visualization with Zeppelin.
Later, you can fully utilize Angular or D3 in Zeppelin for better or more sophisticated visualization.

Let's get the "Bank" data from the official Zeppelin tutorial.

{{ hint_info }}
You can find the tutorial at `Zeppelin Tutorial/Basic Features (Spark)` in the Welcome page.
{{ _hint }}

![zeppelin-data]({{base_path}}/images/teaching/spark_images/zeppelin/prepare.png)

Next, define a `case class` for easy transformation into `DataFrame` and map the text data we downloaded into DataFrame without its header. Finally, register this DataFrame as `Table` to use sql query statements.

![zeppelin-load]({{base_path}}/images/teaching/spark_images/zeppelin/table.png)

## 7. Visualization of Data via SQL query statement

Once data is loaded into `Table`, you can use `SQL` query to visualize data you want to see:

```sql
%sql
<valid SQL statement>
```

Let's try to show a distribution of age of who are younger than 30.

![zeppelin-sql]({{base_path}}/images/teaching/spark_images/zeppelin/sql.png)

As you can see, visualization tool will be automatically loaded once you run a paragraph with SQL statement.
Default one is the result table of the query statement, but you can choose other types of visualization such as bar chart, pie chart and line chart by just clicking the icons.

![zeppelin-charts]({{base_path}}/images/teaching/spark_images/zeppelin/zeppelin_basic.gif)
Also, you can change configurations for each chart as you want

### 7.1. Input Form

You can create input form by using `${formName}` or `${formName=defaultValue}` templates.

![zeppelin-input-form]({{base_path}}/images/teaching/spark_images/zeppelin/input_form.gif)

### 7.2. Select Form

Also, you can create select form by using `${formName=defaultValue,option1|option2...}`

![zeppelin-select-form]({{base_path}}/images/teaching/spark_images/zeppelin/select_form.gif)

For more dynamic forms, please refer to [zeppelin-dynamicform](https://zeppelin.apache.org/docs/latest/manual/dynamicform.html)

## 8. Export/Import Notebook

Once you finish your works, you can export Notebook as JSON file for later use.

![zeppelin-select-form]({{base_path}}/images/teaching/spark_images/zeppelin/export.png)

Also, you can import Notebook exported as JSON or from URL.

![zeppelin-select-form]({{base_path}}/images/teaching/spark_images/zeppelin/import.png)

## Tutorial File

You can download the JSON file for this tutorial [here](https://gist.githubusercontent.com/yuikns/b7fc51a56e936e29f1577456c1b47563/raw/17d25875d7fd73eedaa67bc2f02e0a115110c233/tutorial.json) or see the official 'Zeppelin Tutorial' on the frontpage of Zeppelin.

