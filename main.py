from webapp_template.gen import Generator
import os

url_file = open('urls.txt', 'r')
urls = url_file.readlines()
gen = Generator()

# No data in the urls.txt file
if len(urls) == 0:
    urls = ["/"]

# preparing data to be written to the main app.py file
data = [gen.header]
# populating endpoint handlers
num = 0
for url in urls:
    data.append(gen.endpoints.format(path=url.strip(), number=num))
    num += 1
data.append(gen.footer)

# make directory for webapp
directory="webapp" # name of the directory
copy_dockerfile = "cp webapp_template/Dockerfile webapp/Dockerfile"
copy_requirements = "cp webapp_template/requirements.txt webapp/requirements.txt"

try:
    os.mkdir(directory)
    os.system(copy_dockerfile)
    os.system(copy_requirements)
except:
    print("Some error has occured while copying files from webapp template!")
    exit(0)

with open("webapp/app.py", "w") as app_file:
    for line in data:
        app_file.write(line)
        app_file.write("\n")

print("Script Completed successfully!")