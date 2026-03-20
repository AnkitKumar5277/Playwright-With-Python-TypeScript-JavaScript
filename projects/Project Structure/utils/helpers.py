def take_screenshot(page, name="screenshot"):
    page.screenshot(path=f"reports/{name}.png")