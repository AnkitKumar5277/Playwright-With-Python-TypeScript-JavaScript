# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: todo.spec.js >> test to-to app @sanity
- Location: tests\todo.spec.js:3:5

# Error details

```
Error: expect(locator).toHaveCount(expected) failed

Locator:  locator('.todo-list li')
Expected: 3
Received: 2
Timeout:  5000ms

Call log:
  - Expect "toHaveCount" with timeout 5000ms
  - waiting for locator('.todo-list li')
    9 × locator resolved to 2 elements
      - unexpected value "2"

```

# Page snapshot

```yaml
- generic [ref=e1]:
  - complementary [ref=e2]:
    - generic [ref=e3]:
      - heading "React" [level=3] [ref=e4]
      - generic [ref=e5]:
        - heading "React" [level=5] [ref=e6]
        - link "Source" [ref=e7] [cursor=pointer]:
          - /url: https://github.com/tastejs/todomvc/tree/gh-pages/examples/react
        - heading "TypeScript + React" [level=5] [ref=e8]
        - link "Demo" [ref=e9] [cursor=pointer]:
          - /url: https://todomvc.com/examples/typescript-react
        - text: ","
        - link "Source" [ref=e10] [cursor=pointer]:
          - /url: https://github.com/tastejs/todomvc/tree/gh-pages/examples/typescript-react
    - separator [ref=e11]
    - blockquote [ref=e12]:
      - paragraph [ref=e13]: “ React is a JavaScript library for creating user interfaces. Its core principles are declarative code, efficiency, and flexibility. Simply specify what your component looks like and React will keep it up-to-date when the underlying data changes. ”
      - link "React" [ref=e15] [cursor=pointer]:
        - /url: http://facebook.github.io/react
    - separator [ref=e16]
    - heading "Official Resources" [level=4] [ref=e17]
    - list [ref=e18]:
      - listitem [ref=e19]:
        - link "Quick Start" [ref=e20] [cursor=pointer]:
          - /url: https://react.dev/learn
      - listitem [ref=e21]:
        - link "API Reference" [ref=e22] [cursor=pointer]:
          - /url: https://react.dev/reference/react
      - listitem [ref=e23]:
        - link "Philosophy" [ref=e24] [cursor=pointer]:
          - /url: https://petehuntsposts.quora.com/React-Under-the-Hood
      - listitem [ref=e25]:
        - link "React Community" [ref=e26] [cursor=pointer]:
          - /url: https://react.dev/community
    - heading "Community" [level=4] [ref=e27]
    - list [ref=e28]:
      - listitem [ref=e29]:
        - link "ReactJS on Stack Overflow" [ref=e30] [cursor=pointer]:
          - /url: https://stackoverflow.com/questions/tagged/reactjs
    - generic [ref=e31]:
      - separator [ref=e32]
      - emphasis [ref=e33]:
        - text: If you have other helpful links to share, or find any of the links above no longer work, please
        - link "let us know" [ref=e34] [cursor=pointer]:
          - /url: https://github.com/tastejs/todomvc/issues
        - text: .
  - generic [ref=e35]:
    - generic [ref=e36]:
      - heading "todos" [level=1] [ref=e37]
      - generic [ref=e38]:
        - textbox "New Todo Input" [ref=e39]:
          - /placeholder: What needs to be done?
        - generic [ref=e40]: New Todo Input
    - main [ref=e41]:
      - generic:
        - checkbox "❯ Toggle All Input" [ref=e42]
        - generic: ❯ Toggle All Input
      - list [ref=e43]:
        - listitem [ref=e44]:
          - generic [ref=e45]:
            - checkbox [ref=e46]
            - generic [ref=e47]: Go for walk
            - text: ×
        - listitem [ref=e48]:
          - generic [ref=e49]:
            - checkbox [ref=e50]
            - generic [ref=e51]: Play
            - text: ×
    - generic [ref=e52]:
      - generic [ref=e53]: 2 items left!
      - list [ref=e54]:
        - listitem [ref=e55]:
          - link "All" [active] [ref=e56] [cursor=pointer]:
            - /url: "#/"
        - listitem [ref=e57]:
          - link "Active" [ref=e58] [cursor=pointer]:
            - /url: "#/active"
        - listitem [ref=e59]:
          - link "Completed" [ref=e60] [cursor=pointer]:
            - /url: "#/completed"
      - button "Clear completed" [disabled] [ref=e61] [cursor=pointer]
  - contentinfo [ref=e62]:
    - paragraph [ref=e63]: Double-click to edit a todo
    - paragraph [ref=e64]: Created by the TodoMVC Team
    - paragraph [ref=e65]:
      - text: Part of
      - link "TodoMVC" [ref=e66] [cursor=pointer]:
        - /url: http://todomvc.com
```

# Test source

```ts
  1  | import { test, expect } from '@playwright/test';
  2  | 
  3  | test('test to-to app @sanity', async ({ page }) => {
  4  |   await page.goto('https://todomvc.com/examples/react/dist/');
  5  |   await page.getByTestId('text-input').click();
  6  |   await page.getByTestId('text-input').fill('Buy Grocery');
  7  |   await page.getByTestId('text-input').click();
  8  |   await page.getByTestId('text-input').press('Enter');
  9  |   await page.getByTestId('text-input').fill('Go for walk');
  10 |   await page.getByTestId('text-input').press('Enter');
  11 |   await page.getByTestId('text-input').fill('Rest');
  12 |   await page.getByTestId('text-input').press('Enter');
  13 |   await page.getByTestId('text-input').click();
  14 |   await page.getByTestId('text-input').fill('Play');
  15 |   await page.getByTestId('text-input').press('Enter');
  16 |   await page.getByRole('listitem').filter({ hasText: 'Buy Grocery' }).getByTestId('todo-item-toggle').check();
  17 |   await page.getByRole('listitem').filter({ hasText: 'Rest' }).getByTestId('todo-item-toggle').check();
  18 |   await page.getByRole('link', { name: 'Active' }).click();
  19 |   await page.getByRole('link', { name: 'Completed' }).click();
  20 |   await page.getByRole('link', { name: 'Active' }).click();
  21 |   await expect(page.getByText('Play')).toBeVisible();
  22 |   await expect(page.getByTestId('todo-list')).toContainText('Go for walk');
  23 |   await page.getByRole('button', { name: 'Clear completed' }).click();
  24 |   await page.getByRole('link', { name: 'All' }).click();
> 25 |   await expect(page.locator('.todo-list li')).toHaveCount(3);
     |                                               ^ Error: expect(locator).toHaveCount(expected) failed
  26 | });
```