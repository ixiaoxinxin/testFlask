params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
["%s=%s" % (k, v) for k, v in params.items()]
";".join(["%s=%s" % (k, v) for k, v in params.items()])