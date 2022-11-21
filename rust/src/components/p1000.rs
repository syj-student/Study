use std::io;

pub fn solution() {
    let mut buffer: String = String::new();
    let stdin = io::stdin();

    stdin
    .read_line(&mut buffer)
    .unwrap();

    let answer: i32 = buffer
    .strip_suffix("\n")
    .unwrap()
    .split(' ')
    .map(|x| x.parse::<i32>().unwrap())
    .sum();

    println!("{}", answer);
}