# File: frontend/flutter/lib/main.dart
// Basic app shell
import 'package:flutter/material.dart';

void main() => runApp(MemoriesApp());

class MemoriesApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Memories Collector',
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Memory Frame')),
      body: Center(child: Text('Upload or View Memories')),
    );
  }
}
