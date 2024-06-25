import React from 'react';
import { title } from "@/components/primitives";
import { LineChart } from '@mui/x-charts';
import { ChartContainer } from '@mui/x-charts/ChartContainer';
import { ChartsReferenceLine } from '@mui/x-charts';
import { LinePlot, MarkPlot } from '@mui/x-charts/LineChart';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';

interface LinearGraphProps {
  titleString: string;
  xLables: any;
  xaxisnums: any;
  data: any;
}

const LinearGraph: React.FC<LinearGraphProps> = ({ titleString, xLables, xaxisnums, data }) => {
  return (
    <div className='flex flex-col border-2 border-gray-500 rounded-[35px] items-center justify-center'>
      <div className='p-5 '>
        <h1 className={title({ color: "violet" })}>
          {titleString}
        </h1>
      </div>

      <div>
      <ChartContainer
      width={800}
      height={500}
      series={[
        { data: xaxisnums, label: 'ages', type: 'line' },
        { data: data, label: 'sumofCost', type: 'line' },
      ]}
      xAxis={[{ scaleType: 'point', data: xLables }]}
    >
      <LinePlot />
      <MarkPlot />
      <ChartsXAxis />
      <ChartsYAxis />
    </ChartContainer>
      </div>

    </div>
  );
};

export default LinearGraph;
