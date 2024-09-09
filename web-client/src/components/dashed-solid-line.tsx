'use client'

export const DashedSolidLine = ({
  series,
  lineGenerator,
  xScale,
  yScale,
}: any) => {
  return series.map(({ id, data, color }: any, index: number) => (
    <path
      key={id}
      d={lineGenerator(
        data.map((d: { data: { x: any; y: any } }) => ({
          x: xScale(d.data.x),
          y: yScale(d.data.y),
        })),
      )}
      fill="none"
      stroke={color}
      style={
        index % 2 === 0
          ? {
              // simulate line will dash stroke when index is even
              strokeDasharray: '3, 6',
              strokeWidth: 1,
            }
          : {
              // simulate line with solid stroke
              strokeWidth: 1,
            }
      }
    />
  ))
}
