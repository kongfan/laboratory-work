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

开启代码检查后，可以使用以下命令进行代码检查

:PymodeLint          检查当前标签页中的python代码是否符合规范
:PymodeLintToggle    切换代码检查 ? 
:PymodeLintAuto	     自动修复当前标签页中的PEP8错误

每次在代码修改厚保存都进行代码检查： let g:pymode_lint_on_write = 1

每次在代码修改厚保存都进行代码检查： let g:pymode_lint_unmodified = 0

在编辑代码的时候进行代码检查 ： let g:pymode_lint_on_fly = 0

如果找到错误，自动打开快速修复窗口  let g:pymode_lint_cwindow = 1


支持rope重构

rope是一个Python的重构库，通过这个库你可以实现很多很棒的功能，比如重命名变量，转移模块等等. 用rope重构时，会打开一个对话框，通过对话模式让你选择你要做的操作，为rope的一些选项设定值，当这些操作完成后，你会回到命令提示符，你可以执行重构操作，预览或者取消重构操作。

比如说：我们可以通过rope寻找项目中的文件，RopeFindFile 命令，快捷键 C-x p f,RopecodeAssist 命令（快捷键：M-/)提示自动补全列表，RopeLuckyAssist命令（快捷键：M-？）直接用列表的第一项补全

Keybinding

Uses almost the same keybinding as ropemacs. Note that global commands have a C-x p prefix and local commands have a C-c r prefix. You can change that (see variables section).


C-x p o 	RopeOpenProject
C-x p k 	RopeCloseProject
C-x p f 	RopeFindFile
C-x p 4 f 	RopeFindFileOtherWindow
C-x p u 	RopeUndo
C-x p r 	RopeRedo
C-x p c 	RopeProjectConfig
C-x p n 	[mpfd] 	RopeCreate(Module|Package|File|Directory)
	  	RopeWriteProject
  	 
C-c r r 	RopeRename
C-c r l 	RopeExtractVariable
C-c r m 	RopeExtractMethod
C-c r i 	RopeInline
C-c r v 	RopeMove
C-c r x 	RopeRestructure
C-c r u 	RopeUseFunction
C-c r f 	RopeIntroduceFactory
C-c r s 	RopeChangeSignature
C-c r 1 r 	RopeRenameCurrentModule
C-c r 1 v 	RopeMoveCurrentModule
C-c r 1 p 	RopeModuleToPackage
  	 
C-c r o 	RopeOrganizeImports
C-c r n [vfcmp] RopeGenerate(Variable|Function|Class|Module|Package)
  	 
C-c r a / 	RopeCodeAssist
C-c r a g 	RopeGotoDefinition
C-c r a d 	RopeShowDoc
C-c r a f 	RopeFindOccurrences
C-c r a ? 	RopeLuckyAssist
C-c r a j 	RopeJumpToGlobal
C-c r a c 	RopeShowCalltip
	  	RopeAnalyzeModule
  		RopeAutoImport
  		RopeGenerateAutoimportCache
M-/ 		RopeCodeAssist
M-? 		RopeLuckyAssist
C-c g 		RopeGotoDefinition
C-c d 		RopeShowDoc
C-c f 		RopeFindOccurrences

pymode 支持rope重构，补全及各种辅助操作，开启rope模式： let g:pymode_rope = 1

    :PymodeRopeAutoImport -- Resolve import for element under cursor
    :PymodeRopeModuleToPackage -- Convert current module to package
    :PymodeRopeNewProject -- Open new Rope project in current working directory
    :PymodeRopeRedo -- Redo changes from last refactoring
    :PymodeRopeRegenerate -- Regenerate the project cache
    :PymodeRopeRenameModule -- Rename current module
    :PymodeRopeUndo -- Undo changes from last refactoring
    
.ropeproject 文件夹一般在项目文件夹的上一级目录生成，项目文件夹中所有子目录都利用此.ropeproject 文件夹进行工作。    

通过rope可以很方便的查看光标下对象的文档： let g:pymode_rope_show_doc_bind = '<C-c>d'

rope 补全

一般情况想，同时按下ctrl-space键可以自动补全，按下enter键，第一个提示项会自动插入代码中。按快捷键<C-X><C-O> and <C-P>/<C-N>同样也会达到相同的目的。

查看定义

我们可以按下<C-C>g查看对象的定义 let g:pymode_rope_goto_definition_bind = '<C-c>g'
