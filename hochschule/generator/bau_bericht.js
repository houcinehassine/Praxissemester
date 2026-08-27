// Erzeugt die Tätigkeitsberichte in der Form der OTH-Vorlage.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, ShadingType, PageBreak,
} = require("docx");

const HIER = __dirname;
const daten = JSON.parse(fs.readFileSync(path.join(HIER, "berichtsdaten.json"), "utf8"));

const FONT = "Arial";
const BREITE = 9062;          // Textbreite wie in der Vorlage
const OHNE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const KEINE_RAENDER = { top: OHNE, bottom: OHNE, left: OHNE, right: OHNE };
const UNTERSTRICH = {
  top: OHNE, left: OHNE, right: OHNE,
  bottom: { style: BorderStyle.SINGLE, size: 6, color: "000000" },
};

const t = (text, opt = {}) => new TextRun({ text, font: FONT, size: opt.size || 22,
  bold: !!opt.bold, italics: !!opt.italics, color: opt.color });

const p = (text, opt = {}) => new Paragraph({
  children: Array.isArray(text) ? text : [t(text, opt)],
  alignment: opt.align,
  spacing: { after: opt.after === undefined ? 120 : opt.after, line: opt.line || 276 },
});

// Wertzelle mit Unterstrich + Beschriftungszelle darunter
function feldZeilen(wert, beschriftung, breite) {
  return [
    new TableRow({ children: [ new TableCell({
      width: { size: breite, type: WidthType.DXA }, borders: UNTERSTRICH,
      children: [ p(wert || " ", { after: 20 }) ] }) ] }),
    new TableRow({ children: [ new TableCell({
      width: { size: breite, type: WidthType.DXA }, borders: KEINE_RAENDER,
      children: [ p(beschriftung, { size: 16, color: "595959", after: 140 }) ] }) ] }),
  ];
}

function abschnittsZeile(titel, breite) {
  return new TableRow({ children: [ new TableCell({
    width: { size: breite, type: WidthType.DXA }, borders: KEINE_RAENDER,
    shading: { type: ShadingType.CLEAR, fill: "D9D9D9" },
    children: [ p(titel, { bold: true, after: 60 }) ] }) ] });
}

function feldTabelle(bloecke) {
  const zeilen = [];
  for (const b of bloecke) {
    zeilen.push(abschnittsZeile(b.titel, BREITE));
    for (const f of b.felder) zeilen.push(...feldZeilen(f[0], f[1], BREITE));
  }
  return new Table({ columnWidths: [BREITE], width: { size: BREITE, type: WidthType.DXA },
    borders: KEINE_RAENDER, rows: zeilen });
}

// Kopf eines Tätigkeitsberichts: Nummer, dann Bezeichnung | Zeitraum nebeneinander
function berichtsKopf(nr, titel, zeitraum) {
  const links = 5457, rechts = 3605;
  const zelle = (inhalt, w, rand) => new TableCell({
    width: { size: w, type: WidthType.DXA }, borders: rand, children: inhalt });
  return new Table({
    columnWidths: [links, rechts], width: { size: BREITE, type: WidthType.DXA },
    borders: KEINE_RAENDER,
    rows: [
      new TableRow({ children: [ new TableCell({
        width: { size: BREITE, type: WidthType.DXA }, columnSpan: 2,
        borders: KEINE_RAENDER, shading: { type: ShadingType.CLEAR, fill: "D9D9D9" },
        children: [ p(`Tätigkeitsbericht ${nr}`, { bold: true, after: 60 }) ] }) ] }),
      new TableRow({ children: [
        zelle([ p(titel, { after: 20 }) ], links, UNTERSTRICH),
        zelle([ p(zeitraum, { after: 20 }) ], rechts, UNTERSTRICH) ] }),
      new TableRow({ children: [
        zelle([ p("Bezeichnung der Tätigkeit", { size: 16, color: "595959", after: 140 }) ], links, KEINE_RAENDER),
        zelle([ p("Zeitraum", { size: 16, color: "595959", after: 140 }) ], rechts, KEINE_RAENDER) ] }),
    ]});
}

function endeTabelle(nr) {
  return new Table({ columnWidths: [BREITE], width: { size: BREITE, type: WidthType.DXA },
    borders: { top: { style: BorderStyle.SINGLE, size: 6, color: "000000" },
               bottom: { style: BorderStyle.SINGLE, size: 6, color: "000000" },
               left: { style: BorderStyle.SINGLE, size: 6, color: "000000" },
               right: { style: BorderStyle.SINGLE, size: 6, color: "000000" } },
    rows: [ new TableRow({ children: [ new TableCell({
      width: { size: BREITE, type: WidthType.DXA },
      children: [ p(`Ende Tätigkeitsbericht ${nr}`, { italics: true, after: 0 }) ] }) ] }) ] });
}

const inhalt = [];
inhalt.push(p("Tätigkeitsberichte zum Industriepraktikum",
  { bold: true, size: 30, align: AlignmentType.CENTER, after: 360 }));

inhalt.push(feldTabelle([
  { titel: "Angaben Student", felder: [
    [daten.student.anrede, "Anrede"], [daten.student.vorname, "Vorname"],
    [daten.student.name, "Name"], [daten.student.studiengruppe, "Studiengruppe"],
    [daten.student.matrikelnummer, "Matrikelnummer"], [daten.student.email, "E-Mail"] ] },
  { titel: "Angaben Ausbildungsbetrieb", felder: [
    [daten.betrieb.name, "Name des Betriebes"], [daten.betrieb.anschrift, "Anschrift des Betriebes"],
    [daten.betreuer.anrede, "Anrede Betreuer"], [daten.betreuer.vorname, "Vorname Betreuer"],
    [daten.betreuer.name, "Name Betreuer"], [daten.betreuer.email, "E-Mail Betreuer"],
    [daten.betreuer.telefon, "Telefonnummer Betreuer"] ] },
  { titel: "Übersicht der dokumentierten Tätigkeiten", felder:
      daten.berichte.map((b, i) => [b.titel, `Bezeichnung ${i + 1}. Tätigkeit`]) },
]));

daten.berichte.forEach((b, i) => {
  const nr = i + 1;
  // Jeder Tätigkeitsbericht beginnt auf einer neuen Seite
  inhalt.push(new Paragraph({ children: [ new PageBreak() ] }));
  inhalt.push(berichtsKopf(nr, b.titel, b.zeitraum));
  inhalt.push(p("", { after: 120 }));
  b.absaetze.forEach(a => inhalt.push(p(a, { after: 160 })));
  inhalt.push(p("Beschreibung und Abbildungen", { size: 16, color: "595959", after: 200 }));
  b.abbildungen.forEach(bild => {
    inhalt.push(p(`[ Hier Abbildung einfügen: ${bild.hinweis} ]`,
      { italics: true, color: "808080", align: AlignmentType.CENTER, after: 60 }));
    inhalt.push(p(`Abbildung ${nr}.${bild.nr}: ${bild.text}`,
      { size: 18, align: AlignmentType.CENTER, after: 240 }));
  });
  inhalt.push(endeTabelle(nr));
});

const doc = new Document({
  creator: `${daten.student.vorname} ${daten.student.name}`,
  title: "Tätigkeitsberichte zum Industriepraktikum",
  styles: { default: { document: { run: { font: FONT, size: 22 } } } },
  sections: [ { properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
                children: inhalt } ],
});

const ziel = path.join(path.dirname(HIER), `${daten.dateiname}.docx`);
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(ziel, buf);
  console.log("geschrieben:", ziel, (buf.length / 1024).toFixed(0) + " KB");
});
