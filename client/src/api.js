export function fetchQueryResults(query) { // eslint-disable-line
  return new Promise((resolve, reject) => { // eslint-disable-line
    setTimeout(() => {
      resolve([
        { word: 'test2', id: 2, pos: 'verb' },
        { word: 'test3', id: 3, pos: 'noun' },
        { word: 'test1', id: 1, pos: 'adjective' },
      ]);
    }, 3000);
  });
}

export function fetchDefinitionByID(id) {
  // eslint-disable-next-line
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({
        id,
        word: `test${id}`,
        definition: `This is the definition for the word with ID ${id}.`,
      });
    }, 3000);
  });
}
