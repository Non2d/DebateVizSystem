import React from 'react';
import {Handle, Position} from "reactflow";

const GovNode = ({ data }) => {
  return (
    <div className="w-32 h-2 bg-red-500">
      <Handle type="target" id="tgt" position={Position.Right} className="w-1 h-1 bg-red-500" />
      <Handle type="source" id="src" position={Position.Right} className="w-1 h-1 bg-red-500" />
    </div>
  );
};

export default GovNode;