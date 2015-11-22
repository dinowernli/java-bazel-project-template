package org.example.library;

import com.google.common.collect.ImmutableList;

public class HelloFormatter {
  private static final ImmutableList<String> GREETINGS = ImmutableList.of(
      "Hello", "Greetings");

  public String format(String name) {
    return pickGreeting(name) + ", " + name;
  }

  private String pickGreeting(String name) {
    int hash = name.length();
    return GREETINGS.get(hash % GREETINGS.size());
  }
}
