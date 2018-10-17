#include "common.hpp"

using snake_t = std::vector<std::pair<int, int> >;
using pos_t = std::pair <int, int>;

int move_to(int new_dir, int dir){
  switch(new_dir){
    case 'w':
      (dir != 's') ? dir = 'w' : dir = 's';
    break;
    case 'a':
      (dir != 'd') ? dir = 'a' : dir = 'd';
    break;
    case 's':
      (dir != 'w') ? dir = 's' : dir = 'w';
    break;
    case 'd':
      (dir != 'a') ? dir = 'd' : dir = 'a';
    break;
  }

  return dir;
}

void delete_snake(snake_t &snake){

}

void print_snake(snake_t &snake){
  int x,y;
  for (auto piece : snake){
    x = piece.first;
    y = piece.second;
    mvprintw(y, x, "#");
  }
}

void move_snake(int dir, snake_t &snake){
  //Quitar el simbolo de la primera  posicion
  //Mirar la dirección que me dan y la última posicion y pnitar el simbolo
  // dependiendo de la direccion

  int x,y;
  x = snake.front().first;
  y = snake.front().second;
  mvprintw(y,x, " ");
  snake.erase(snake.begin());

  pos_t last_pos = snake.back();
  pos_t new_pos;

  if (dir == 'w'){
    new_pos = std::make_pair(last_pos.first, last_pos.second-1);
  }
  if (dir == 'a'){
    new_pos = std::make_pair(last_pos.first-1, last_pos.second);
  }
  if (dir == 's'){
    new_pos = std::make_pair(last_pos.first, last_pos.second+1);
  }
  if (dir == 'd'){
    new_pos = std::make_pair(last_pos.first+1, last_pos.second);
  }

  snake.push_back(new_pos);
  x=last_pos.first;
  y=last_pos.second;
  mvprintw(y,x, "#");
}


int main (void){
  //Declaraciones
  WINDOW * mainwin;
  int dir = 's';
  int new_dir;
  int maxx, maxy;
  int gamestatus = PLAYING;
  getmaxyx(mainwin, maxy, maxx);
  // coordenadas {y, x}
  snake_t snake {{10,10}, {10, 11}, {10, 12}, {10, 13}, {10, 14}, {10, 15}, {10, 16}};


  /*  Initialize ncurses  */
  if ( (mainwin = initscr()) == NULL ) {
    fprintf(stderr, "Error initializing ncurses.\n");
    exit(EXIT_FAILURE);
  }
  noecho();                  /*  Que cuando escribes una letra no salga en la pantalla */
  cbreak();                   /* Hacer que las letras stén disponibles sin pulsar enter*/
  keypad(mainwin, TRUE);     /*  Enable the keypad for non-char keys  */
  curs_set(0);               /*  Turn off cursor blinkning */
  nodelay(mainwin, TRUE);                 /* Hacer que getch sea no bloqueante*/
  /*  ncurses Initialized */

  mvprintw(0,0, "Max x is %i and max y is %i", getmaxx(mainwin), getmaxy(mainwin));

  //Main loop
  print_snake(snake);
  while( gamestatus == PLAYING ){

    if ((new_dir = getch()) != ERR){
      if (new_dir == 'q'){
        gamestatus = GAME_OVER;
      }
      else {
        dir = move_to(new_dir, dir);
      }
    }
    refresh();
    usleep(50000);

    move_snake(dir, snake);

    //Info
    getmaxyx(mainwin, maxy, maxx);
    // mvprintw(0, 0, "(%i,%i) ", maxx, maxy);
    // mvprintw(1, 0, "(%i,%i) ", x,   y);
    mvprintw(2, 0, "current dir %c, new dir %c", dir, new_dir);
    //Info
  }
  nodelay(mainwin, FALSE);
  getch();

  /*  Clean up after ourselves  */
  delwin(mainwin);
  endwin();
  refresh();

  return EXIT_SUCCESS;
}
