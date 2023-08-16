import click
from biliarchiver.i18n import _
from biliarchiver.cli_tools.up_command import up
from biliarchiver.cli_tools.down_command import down
from biliarchiver.cli_tools.get_command import get
from biliarchiver.version import BILI_ARCHIVER_VERSION


class HelpCommand(click.Group):
    def format_help(self, ctx, formatter):
        version_info = click.style(
            f"[ biliarchiver {BILI_ARCHIVER_VERSION} ]",
            fg="black",
            bg="white",
            bold=True,
            blink=True,
        )
        click.echo(
            f"""
                <_-^-_>
       <%&&&&&&&&&&&&&&&&&&&&%*>
 <&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&>      > __      __   __   __       <
  /<&&&>     <&&&>/      .<&&&>      <&&&>  >      / /     /_/  / /  /_/ <
  (<&&&>,(/(/<&&&>%(/(/(/(<&&&>(/(// <&&&>  >     / /_    __   / /  __   <
  %<&&&>((   <&&&#>      <#&&&>   (((<&&&(> >    / __ \  / /  / /  / /   <
  <&&&&>/*   <&&&#>,    .<#&&&>   .//<&&&(> >   / /_/ / / /  / /  / /   __      __   <
  <&&&&>(* ,(<&&&#>%    %<#&&&>%(  ((<&&&(> >  /_.___/ /_/  /_/  /_/   / /     /_/   <
  <&&&&>/*  .<&&&#>      <#&&&>%   (/<&&&(> >    ____ _  ____  _____  / /_    __  _   __  ___    ____ <
  (<&&&>(*   <&&&>#,,-w-,#<&&&>    ((<&&&(> >   / __ `/ / __/ / ___/ / __ \  / / | | / / / _ \  / __/ <
  (<&&&>/*   <&&&>,       <&&&>   .//<&&&)> >  / /_/ / / /   / /__  / / / / / /  | |/ / /  __/ / / <
   <&&&>((/((<&&&>((((((((<&&&>(((/((<&&&>  >  \__,_/ /_/    \___/ /_/ /_/ /_/   |___/  \___/ /_/  <
   <&&&>  ,,(<&&&>        <&&&>(,,   <&&&>
  <&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&>               {version_info}
<&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&><""".replace(
                "<", "\u001b[0m"
            ).replace(
                ">", "\u001b[96m"
            ),
        )
        click.echo(super().format_help(ctx, formatter))


@click.group(cls=HelpCommand)
def biliarchiver():
    pass


@biliarchiver.command(help=click.style(_("初始化所需目录"), fg="cyan"))
def init():
    import pathlib

    biliarchiver_home = pathlib.Path.cwd() / "biliarchiver.home"
    bilibili_archive_dir = pathlib.Path.cwd() / "bilibili_archive_dir"
    biliarchiver_home.mkdir(exist_ok=True)
    bilibili_archive_dir.mkdir(exist_ok=True)


biliarchiver.add_command(up)
biliarchiver.add_command(down)
biliarchiver.add_command(get)


@biliarchiver.command(help=click.style(_("配置账号信息"), fg="cyan"))
def auth():
    click.echo(click.style("Bilibili", bg="yellow"))
    click.echo(_("登录后将哔哩哔哩的 cookies 复制到 `config.json` 指定的文件（默认为 `~/.cookies.txt`）中。"))
    click.echo("")
    click.echo(click.style("Internet archive", bg="yellow"))
    click.echo(_("前往 https://archive.org/account/s3.php 获取 Access Key 和 Secret Key。"))
    click.echo(_("""将它们放在 `config.json` 指定的文件（默认为 `~/.bili_ia_keys.txt`）中，两者由换行符分隔。"""))
    


if __name__ == "__main__":
    biliarchiver()
