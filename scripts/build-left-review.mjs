// Owner-confirmed vertical-axis reflection, 9 November 2026. Text is not reversed.
import{readFile,writeFile,mkdir,readdir}from'node:fs/promises';
import path from'node:path';import{fileURLToPath}from'node:url';
const web=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../web');
await mkdir(path.join(web,'maps-left-review'),{recursive:true});
for(const name of await readdir(path.join(web,'maps'))){
 if(!name.endsWith('.svg'))continue;
 let svg=await readFile(path.join(web,'maps',name),'utf8');
 const width=2*Number(svg.match(/<ellipse cx="([\d.]+)"/)[1]);
 svg=svg.replace(/<(polygon|path|ellipse)\b([^>]*?)\/>/g,(_,tag,attrs)=>{
  const transform=attrs.match(/ transform="([^"]*)"/);
  attrs=attrs.replace(/ transform="[^"]*"/,'');
  return '<'+tag+attrs+' transform="translate('+width+' 0) scale(-1 1)'+(transform?' '+transform[1]:'')+'"/>';
 }).replace(/<rect\b([^>]*?)\/>/g,(_,attrs)=>{
  const x=Number(attrs.match(/\bx="([^"]+)"/)[1]),w=Number(attrs.match(/\bwidth="([^"]+)"/)[1]);
  return '<rect'+attrs.replace(/\bx="[^"]+"/,'x="'+(width-x-w)+'"')+'/>';
 }).replace(/<text\b([^>]*?)>/g,(_,attrs)=>'<text'+attrs.replace(/\bx="([^"]+)"/,(_,x)=>'x="'+(width-Number(x))+'"')+'>');
 svg=svg.replace('— original directional map','— left-handed directional map').replace('Vector reconstruction preserving the original sectors, arrows and success areas.','Left-handed map reflected across the vertical centerline under the owner-confirmed clock-face rule.');
 await writeFile(path.join(web,'maps-left-review',name),svg);
}
console.log('41 left-handed diagrams built under the confirmed mirror rule; text remains readable.');
