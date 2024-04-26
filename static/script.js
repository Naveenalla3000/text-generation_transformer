const promptSuggestions = document.querySelectorAll('.promt-suggestion');
promptSuggestions.forEach(suggestion => {
  suggestion.addEventListener('click', (event) => {
    document.querySelector('input[name="text"]').value = event.target.textContent;
    document.querySelector('form').submit();
    document.querySelector('.loader').style.display = 'block';
  });
});
function loading(){
    document.querySelector('.loader').style.display = 'block';
}
