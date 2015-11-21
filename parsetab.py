
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = "\xb8\xbei\xec\x8c\x82\x05'Y\xdc}\x87\x8a*\x95\xc5"
    
_lr_action_items = {'C':([6,7,10,13,14,15,16,18,],[-11,-12,-10,-9,-8,18,-7,-6,]),'E':([4,],[5,]),'D':([4,5,6,7,8,10,11,],[6,6,6,6,6,6,6,]),'G':([4,5,6,7,8,10,11,],[7,7,7,7,7,7,7,]),'COLOR':([5,],[11,]),'NUMBER':([0,],[2,]),'S':([4,5,6,7,8,10,11,],[8,8,8,8,8,8,8,]),'ID':([0,4,5,6,7,8,10,11,],[4,10,10,10,10,10,10,10,]),'$end':([1,2,3,4,6,7,9,10,12,13,14,16,17,18,],[0,-13,-3,-4,-11,-12,-5,-10,-2,-9,-8,-7,-1,-6,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'A':([0,],[1,]),'W':([4,5,6,7,8,10,11,],[9,12,13,14,15,16,17,]),'N':([0,],[3,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> A","S'",1,None,None,None),
  ('A -> ID E COLOR W','A',4,'p_raiz','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',37),
  ('A -> ID E W','A',3,'p_raiz1','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',43),
  ('A -> N','A',1,'p_raiz2','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',49),
  ('A -> ID','A',1,'p_raiz3','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',58),
  ('A -> ID W','A',2,'p_raiz4','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',64),
  ('W -> S W C','W',3,'p_W','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',70),
  ('W -> ID W','W',2,'p_SW','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',74),
  ('W -> G W','W',2,'p_SW','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',75),
  ('W -> D W','W',2,'p_SW','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',76),
  ('W -> ID','W',1,'p_ID','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',80),
  ('W -> D','W',1,'p_ID','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',81),
  ('W -> G','W',1,'p_ID','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',82),
  ('N -> NUMBER','N',1,'p_number','/home/erick/Desktop/U/VI_Semestre/Automatas/SistemasLyPS4/lsystems/lsystem.py',86),
]
