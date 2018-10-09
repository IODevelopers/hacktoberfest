const capitalize = (string) => {
  return string.split(" ").map(word => {
    return word.split("").map(letter => {
      return letter.toUpperCase();
    }).join('')
  }).join(' ')
}

console.log(capitalize("this is america."))