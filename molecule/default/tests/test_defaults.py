import pytest

def test_fabricmc_install_dir(host):

    fabmc_install_dir = host.file('/opt/fabricmc')
    assert fabmc_install_dir.exists
    assert fabmc_install_dir.is_directory
    assert fabmc_install_dir.mode == 0o755

def test_install_bin_dir(host):

    install_bin_dir = host.file('/opt/fabricmc/bin')
    assert install_bin_dir.exists
    assert install_bin_dir.is_directory
    assert install_bin_dir.mode == 0o755

def test_install_workspace_dir(host):

    install_workspace_dir = host.file('/opt/fabricmc/workspace')
    assert install_workspace_dir.exists
    assert install_workspace_dir.is_directory
    assert install_workspace_dir.mode == 0o755

def test_server_launcher_jar_file(host):

    server_jar_file = host.file('/opt/fabricmc/bin/minecraft_server_launcher.1.21.4-0.16.10-1.0.1.jar')
    assert server_jar_file.exists
    assert server_jar_file.is_file
    assert server_jar_file.mode == 0o644

def test_server_launcher_jar_symlink(host):

    server_jar_symlink = host.file('/opt/fabricmc/bin/minecraft_server_launcher.jar')
    assert server_jar_symlink.exists
    assert server_jar_symlink.is_symlink

def test_server_launcher_start_script(host):

    server_start_script = host.file('/opt/fabricmc/bin/start.sh')
    assert server_start_script.exists
    assert server_start_script.is_file
    assert server_start_script.mode == 0o755
    assert server_start_script.contains('java -Xmx2048M -Xms1024M -jar /opt/fabricmc/bin/minecraft_server_launcher.jar nogui')
