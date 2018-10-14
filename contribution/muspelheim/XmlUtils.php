<?php

/**
 * Class XmlUtils
 */
class XmlUtils
{
    /**
     * @param \SimpleXMLElement $xml
     * @return array
     */
    public static function xml2array($xml)
    {
        $arr = [];
        if (null !== $xml) {
            /** @var \SimpleXMLElement $r */
            foreach ($xml->children() as $r) {
                if (\count($r->attributes()) > 0) {
                    $res = [];

                    foreach ($r->attributes() as $key => $val) {
                        $res[(string)$key] = (string)$val;
                    }

                    $arr[$r->getName()][] = $res;
                } else {
                    if (\count($r->children()) === 0) {
                        $arr[$r->getName()] = (string)$r;
                    } else {
                        $arr[$r->getName()][] = static::xml2array($r);
                    }
                }
            }
        }

        return $arr;
    }
}
