def function_a():
    print("function_aの内部の命令文です")


print("これからfunction_aを呼び出します")
function_a()
print("function_aの呼び出しが終わりました")


def function_b():
    print("function_bの処理開始")
    function_a()
    print("function_bの処理終了")


print("function_bを呼び出します")
function_b()
