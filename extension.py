import vscode
from vscode import InfoMessage

ext = vscode.Extension(name="Abracadabra")

@ext.event
async def on_activate():
    vscode.log(f"The Extension '{ext.name}' has started")


@ext.command()
async def do_magic(ctx):
    try:
        active_text_editor = await ctx.window.active_text_editor
        file_path = active_text_editor.document.fileName
        # get file name from path
        import os
        file_directory = os.path.dirname(file_path)
        file_name = file_path.split('\\')[-1]
        file_name_ = file_name.split('.')[0]

        template1 = f'import {file_name_}'
        template2 = f'from {file_name_} import'
        # check if file name is imported
        with open(file_path, 'r') as f:
            content = f.read()
            if template1 in content or template2 in content:
                # rename file
                if 0:
                    new_path = os.path.join(file_directory, f'my_{file_name}')
                    cmd =f"vscode.workspace.fs.rename( vscode.Uri.file('{file_path}'), vscode.Uri.file('{new_path}'))"
                    vscode.log(cmd)
                    await ctx.ws.run_code(cmd,  thenable=False)
                msg = 'Don\'t use module name as file name!'
            else:
                msg = 'Need more Abracadabra! 🧙‍♂️ Join the OverflowAI Search waitlist '
                url ='https://stackoverflow.co/labs/search'
                import webbrowser
                webbrowser.open(url)

        # output_channel = await ctx.ws.run_code('')

        return await ctx.show(InfoMessage(msg))
    except Exception as e:
        from pymsgbox import alert
        alert(str(e), "Error")
ext.run()
