# -*- mode: python -*-

block_cipher = None


a = Analysis(['menu.py'],
             pathex=['C:\\Users\\ewahe\\OneDrive\\Dokumenty\\planetbox-master\\src'],
             binaries=[],
             datas=[],
             hiddenimports=['thorpy.elements._wrappers.make_button', 'thorpy.elements.Checker'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Planetbox',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='C:\\Users\\ewahe\\OneDrive\\Dokumenty\\planetbox-master\\imgs\\favicon.ico')
