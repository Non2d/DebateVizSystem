import { BaseEdge, getBezierPath, getStraightPath, getSmoothStepPath, getSimpleBezierPath } from 'reactflow';

export default function CustomEdge({ id, sourceX, sourceY, targetX, targetY }) {
  const [edgePath] = getStraightPath({
    sourceX,
    sourceY,
    targetX,
    targetY,
  });

  return (
    <>
      <BaseEdge id={id} path={edgePath} style={{ stroke: 'red', strokeWidth: 2 }} />
    </>
  );
}
