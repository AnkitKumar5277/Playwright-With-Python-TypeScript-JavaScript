# To-do App Automation
Demo App : https://todomvc.com/examples/react/dist/  
Automate core Todo actions (add, complete, delete) on the TodoMVC app  

### Tools
- Node.js
- Playwright (use latest if possible)
- VS Code (or any editor)

### End Result
A working Playwright Test that runs locally, produces an HTML report, and a screenshot showing the final todo list

### Project Goals (measurable)
1. Install Playwright and create tests
2. Automate adding 3 todos, mark 1 as completed, delete
3. Generate Playwright HTML report and open it
4. Add assertions and check failure in report
5. Take screenshots and video on failure and attach to report
6. Run with interactive UI
7. Run in debug mode
8. Run with trace on

### Setup
1. Create project folder and initialize npm
npm init -y
(npm init -y creates package.json)
2. Install Playwright Test (dev dependency) and install browsers:
npm init playwright@latest
npx playwright install
(npx playwright install downloads Chromium/Firefox/WebKit used by Playwright)
3. Create:
tests/todo.spec.ts (TypeScript)
or
tests/todo.spec.js (JavaScript)
