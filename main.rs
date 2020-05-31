use std::env;
use std::process::{Command};
use walkdir::WalkDir;

fn main(){
    let mut hashcat = String::from("");
    let mut output;

    for arg in env::args().skip(1) {
        for x in WalkDir::new(arg).into_iter().filter_map(Result::ok).filter(|e| !e.file_type().is_dir()) {
            output = Command::new("md5sum")
            .arg(x.path().display().to_string())
            .output()
            .expect("failed to execute process");
            for e in String::from_utf8_lossy(&output.stdout).to_string().split_whitespace().next(){
                hashcat = format!("{}{}", hashcat, e.to_string());
            }
        }
    }

    let digest = md5::compute(hashcat.into_bytes());

    println!("{}", format!("{:x}", digest)); 
} 