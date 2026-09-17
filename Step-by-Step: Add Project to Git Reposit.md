Step-by-Step: Add Project to Git Repository

1. Create a .gitignore file first (important!)

Create a .gitignore file in your project root to protect sensitive files:

.env
**pycache**/
\*.pyc
node_modules/

2. Initialize Git in your project
   cd /Users/seemamahur/making_a_request
   git init

3. Add your files to staging
   git add .

4. Make your first commit
   git commit -m "Initial commit"

5. Create a new repository on GitHub/GitLab

6. Connect your local repo to remote
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git

7. Push your code
   git branch -M main
   git push -u origin main
