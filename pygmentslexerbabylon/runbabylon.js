var babylon = require("babylon");
var input = '';
var ret = [];
var i;

process.stdin.setEncoding('utf8');
process.stdin.on('data', function (chunk) {
  input += chunk;
});
process.stdin.on('end', function () {
  var ast  = babylon.parse(input, {
    sourceType: 'module',
    allowImportExportEverywhere: true,
    allowReturnOutsideFunction: true,
    plugins: [
      'asyncFunctions',
      'asyncGenerators',
      'classConstructorCall',
      'classProperties',
      'decorators',
      'doExpressions',
      'exponentiationOperator',
      'exportExtensions',
      'flow',
      'functionSent',
      'functionBind',
      'jsx',
      'objectRestSpread',
      'trailingFunctionCommas'
    ]
  });

  var tokens = ast.tokens;
  for (i = 0; i < tokens.length; i = i + 1) {
    var t = tokens[i];
    var type;
    type = t.type.label ? t.type.label : t.type;
    ret.push([t.start, t.end, type]);
  }
  console.log(JSON.stringify(ret));
});
