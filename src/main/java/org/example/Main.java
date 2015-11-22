package org.example;

import org.example.library.HelloFormatter;

public class Main {
  public static void main(String[] args) {
    HelloFormatter formatter = new HelloFormatter();

    System.out.println(formatter.format("there"));
  }
}
