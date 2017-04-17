学习pymode的心得

pymode 是一个vim插件，它能让我们方便的在vim中进行python 开发

pymode 有以下特点：

1. 支持python2.6+及python3.2+
2. 支持语法高亮
3. 支持虚拟环境 Virtualenv 
4. 快捷键<leader>+r 直接运行python 代码
5. 快捷键<leader>+b 设置断点，调试python 代码
6. 优化python缩进
7. python 
8. python 代码快速移动 (``]]``, ``3[[``, ``]]M``, ``vaC``, ``viM``, ``daC``, ``ciM``, ...)
9. python 代码检查(pylint,pyflakes, pylama, 使用 (``:PymodeLint``)实时检查
10. 自动修复pep8错误，使用(``:PymodeLintAuto``)命令
11.  查看python文档 ，使用(``K``)命令
12. 代码重构 <rope refactoring library> (rope)
13. 自动补全 (rope)
14. 转跳到自定义处，快捷键：(``<C-c>g`` for `:RopeGotoDefinition`)

配置pymode

我们可以再vimrc文件中配置pymode，pymode有丰富的选项供我们灵活配置

开启pymode 模式  ： 在vimrc中添加一行 let g:pymode = 1
关闭pymode的警告 ： 在vimrc中添加一行 let g:pymode_warnings = 1
添加系统路径     ： 在vimrc中添加一行 let g:pymode_paths = []
删除无用空格     ： 在vimrc中添加一行 let g:pymode_trim_whitespaces = 1
开启python模式   ： 在vimrc中添加一行 let g:pymode_options = 1

    setlocal complete+=t
    setlocal formatoptions-=t
    if v:version > 702 && !&relativenumber
        setlocal number
    endif
    setlocal nowrap
    setlocal textwidth=79
    setlocal commentstring=#%s
    setlocal define=^\s*\\(def\\\\|class\\)

设置每行最多字数的位置是否为彩色列 一般是79个字符的位置为红色 let g:pymode_options_colorcolumn = 1

设置快速修复窗口的大小 let g:pymode_quickfix_minheight = 3 ;  let g:pymode_quickfix_maxheight = 6

设置python的版本，是python2还是python3 :let g:pymode_python = 'python'; let g:pymode_python = 'python3' 

设置兼容pep8的python缩进， let g:pymode_indent = 1

设置python代码折叠  let g:pymode_folding = 1

vim 中快速移动

开启pymode 快速移动模式 :  let g:pymode_motion = 1

`C` — 表示类
`M` — 表示函数

下面是一些快速移动的快捷键, 通过这些快捷键可以在python代码中快速移动

    ================================================================================

    [[      Jump to previous class or function (normal, visual, operator modes)
    ]]      Jump to next class or function  (normal, visual, operator modes)
    [M      Jump to previous class or method (normal, visual, operator modes)
    ]M      Jump to next class or method (normal, visual, operator modes)
    aC      Select a class. Ex: vaC, daC, yaC, caC (normal, operator modes)
    iC      Select inner class. Ex: viC, diC, yiC, ciC (normal, operator modes)
    aM      Select a function or method. Ex: vaM, daM, yaM, caM (normal, operator modes)
    iM      Select inner function or method. Ex: viM, diM, yiM, ciM (normal, operator modes)

    ==================================================================================== 

pymode能够让我们在编写代码是快速检索函数或类的文档说明，通过pydoc 展示当前光标下对象的文档帮助类容， :PymodeDoc<args> — show documentation 


设置开启pymode_doc   :  let g:pymode_doc = 1, 文档 模式开启后我们可以快速查看pydoc

设置开启pymode_doc快捷键   :  let g:pymode_doc_bind = 'K' ,设置快捷键为 K

设置支持virtualenv，virtualenv就是用来为一个应用创建一套“隔离” 的 python运行环境  let g:pymode_virtualenv = 1

手工设置virtualenv 路径， let g:pymode_virtualenv_path = $VIRTUAL_ENV


运行python代码

开启代码运行模式： let g:pymode_run = 1 ，设置代码运行快捷键： let g:pymode_run_bind = '<leader>r'
开启代码调试模式： let g:pymode_breakpoint = 1 ，设置代码调试快捷键： let g:pymode_breakpoint_bind = '<leader>b'

检查python代码


开启代码检查： let g:pymode_lint = 1

每次在代码修改厚保存都进行代码检查： let g:pymode_lint_on_write = 1

每次在代码修改厚保存都进行代码检查： let g:pymode_lint_unmodified = 0

在编辑代码的时候进行代码检查 ： let g:pymode_lint_on_fly = 0

如果找到错误，自动打开快速修复窗口  let g:pymode_lint_cwindow = 1


支持rope重构

pymode 支持rope重构，补全及各种辅助操作，开启rope模式： let g:pymode_rope = 1

    :PymodeRopeAutoImport -- Resolve import for element under cursor
    :PymodeRopeModuleToPackage -- Convert current module to package
    :PymodeRopeNewProject -- Open new Rope project in current working directory
    :PymodeRopeRedo -- Redo changes from last refactoring
    :PymodeRopeRegenerate -- Regenerate the project cache
    :PymodeRopeRenameModule -- Rename current module
    :PymodeRopeUndo -- Undo changes from last refactoring
    
    
