#steps to take when creating new project

git clone https://github.com/yourusername/django-starter.git estate-management
cd estate-management
rm -rf .git          # cut the link to the starter repo
git init             # start a fresh git history for the new project
git add .
git commit -m "init from django-starter"
