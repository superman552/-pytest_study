# //*[@text="联系人"]/../..//*[@text=f"{text}"]

def aa(text):
    print(12)
    print(f'//*[@text="联系人"]/../..//*[@text="{text}"]')
    print(f'newUiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));')

aa(122)
