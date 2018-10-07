package com.example.nomitpahuja.tables;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.SeekBar;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final ArrayList<Integer> table = new ArrayList<Integer>();
        SeekBar seekBar = (SeekBar)findViewById(R.id.seekBar);
        final ListView tables = (ListView)findViewById(R.id.tables);
        seekBar.setMax(20);
        seekBar.setProgress(10);
        for(int i=0;i<10;i++){
            table.add((i+1)*seekBar.getProgress());
        }
        ArrayAdapter<Integer> arrayAdapter = new ArrayAdapter<Integer>(getApplicationContext(),android.R.layout.simple_list_item_1,table);
        tables.setAdapter(arrayAdapter);
        seekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                int min = 1;
                if(progress<min){
                    progress = min;
                    seekBar.setProgress(min);
                }
                table.clear();
                for(int i=0;i<10;i++){
                    table.add((i+1)*progress);
                }
                ArrayAdapter<Integer> arrayAdapter = new ArrayAdapter<Integer>(getApplicationContext(),android.R.layout.simple_list_item_1,table);
                tables.setAdapter(arrayAdapter);
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });
    }
}
