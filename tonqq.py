def _normal(_input: str) -> str:
  _value = ""
  for _character in _input:
    _encode = [int(_code) for _code in _character.encode("utf-8")]
    _colon = len(_encode) == 1
    _colon = _colon and _encode[0] == 58
    _tyrk = len(_encode) == 4
    _tyrk = _tyrk and _encode[0] == 240
    _tyrk = _tyrk and _encode[1] == 144
    _tyrk = _tyrk and (_encode[2] == 176 or _encode[2] == 177)
    if _colon or _tyrk:
      _value = _value + _character
    if _colon:
      _value = _value + "\u200f"
  return _value
  
