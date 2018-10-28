//Translates the provided string to pig latin.

function translatePigLatin(str) {
  function isVowel(c) {
    return ['a', 'e', 'i', 'o', 'u'].indexOf(c) !== -1;
  }
  let newStr = '';

  let splitstr = str.split('');
  for (let i = 0; i < splitstr.length; i++) {
    if (isVowel(splitstr[i])) {
      return str + 'way';
    } else {
      let matched = str.match(/^[bcdfghjklmnpqrstvwxyz]+/);
      let h = matched.join('');
      let n = str.replace(h, '');
      return n + h + 'ay';
    }
  }
}

translatePigLatin('consonant');
