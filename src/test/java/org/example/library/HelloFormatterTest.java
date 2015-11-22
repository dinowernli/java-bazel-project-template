package org.example.library;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

public class HelloFormatterTest {
  private HelloFormatter formatter;

  @Before
  public void setUp() {
    formatter = new HelloFormatter();
  }

  @Test
  public void usesGreetings() {
    assertEquals("Greetings, world", formatter.format("world"));
  }

  @Test
  public void usesHello() {
    assertEquals("Hello, Mark", formatter.format("Mark"));
  }
}

